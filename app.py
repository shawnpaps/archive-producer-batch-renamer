import streamlit as st
import os
import re
from pathlib import Path
from typing import List, Dict, Tuple
import shutil

st.set_page_config(
    page_title="Archive Producer Batch Renamer",
    page_icon="🎵",
    layout="wide"
)

def parse_filename(filename: str) -> Dict[str, str]:
    """
    Parse a filename to extract potential components.
    This is a basic parser that can be enhanced based on your specific patterns.
    """
    # Remove file extension
    name_without_ext = Path(filename).stem
    
    # Common patterns in music production
    patterns = {
        'song_name': r'^([a-zA-Z0-9_]+?)(?:_(?:prod|mix|master|final|v\d+|version\d+))',
        'artist_name': r'(?:^|_)([a-zA-Z0-9_]+?)(?:_(?:prod|mix|master|final|v\d+|version\d+))',
        'version': r'(?:prod|mix|master|final|v\d+|version\d+)',
        'version_number': r'(\d+)'
    }
    
    parsed = {}
    
    # Try to extract song name
    song_match = re.search(patterns['song_name'], name_without_ext, re.IGNORECASE)
    if song_match:
        parsed['song_name'] = song_match.group(1).replace('_', ' ')
    
    # Try to extract version info
    version_match = re.search(patterns['version'], name_without_ext, re.IGNORECASE)
    if version_match:
        parsed['version'] = version_match.group(0)
    
    # Try to extract version number
    version_num_match = re.search(patterns['version_number'], name_without_ext)
    if version_num_match:
        parsed['version_number'] = version_num_match.group(1)
    
    return parsed

def generate_new_name(filename: str, template: str, custom_mappings: Dict[str, str] = None) -> str:
    """
    Generate a new filename based on the template and parsed components.
    """
    parsed = parse_filename(filename)
    
    # Apply custom mappings if provided
    if custom_mappings:
        parsed.update(custom_mappings)
    
    # Replace placeholders in template
    new_name = template
    for key, value in parsed.items():
        placeholder = f"{{{key}}}"
        if placeholder in new_name:
            new_name = new_name.replace(placeholder, str(value) if value else '')
    
    # Clean up any remaining placeholders
    new_name = re.sub(r'\{[^}]+\}', '', new_name)
    
    # Clean up extra underscores and spaces
    new_name = re.sub(r'_+', '_', new_name)
    new_name = re.sub(r'\s+', ' ', new_name)
    new_name = new_name.strip('_ ')
    
    return new_name

def main():
    st.title("🎵 Archive Producer Batch Renamer")
    st.markdown("Rename your music production folders with consistent naming conventions")
    
    # Sidebar for configuration
    with st.sidebar:
        st.header("Configuration")
        
        # Template input
        st.subheader("Naming Template")
        template = st.text_input(
            "Template (use {song_name}, {artist_name}, {version}, {version_number})",
            value="{song_name}_{artist_name}_{version}_{version_number}",
            help="Use placeholders in curly braces to define your naming pattern"
        )
        
        # Custom mappings
        st.subheader("Custom Mappings")
        custom_artist = st.text_input("Default Artist Name (if not found in filename)")
        custom_version = st.text_input("Default Version (if not found in filename)")
        
        custom_mappings = {}
        if custom_artist:
            custom_mappings['artist_name'] = custom_artist
        if custom_version:
            custom_mappings['version'] = custom_version
    
    # Main content area
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.header("📁 Select Directory")
        
        # Directory input
        directory = st.text_input(
            "Enter directory path:",
            placeholder="/path/to/your/music/projects"
        )
        
        if directory and os.path.exists(directory):
            st.success(f"✅ Directory found: {directory}")
            
            # Get all folders in directory
            folders = [f for f in os.listdir(directory) if os.path.isdir(os.path.join(directory, f))]
            
            if folders:
                st.subheader(f"Found {len(folders)} folders:")
                
                # Preview changes
                preview_data = []
                for folder in folders:
                    old_name = folder
                    new_name = generate_new_name(folder, template, custom_mappings)
                    preview_data.append({
                        "Original": old_name,
                        "New Name": new_name,
                        "Changed": old_name != new_name
                    })
                
                # Display preview
                st.dataframe(
                    preview_data,
                    use_container_width=True,
                    column_config={
                        "Changed": st.column_config.CheckboxColumn("Changed?")
                    }
                )
                
                # Rename button
                if st.button("🚀 Apply Renames", type="primary"):
                    with st.spinner("Renaming folders..."):
                        success_count = 0
                        error_count = 0
                        
                        for folder in folders:
                            old_path = os.path.join(directory, folder)
                            new_name = generate_new_name(folder, template, custom_mappings)
                            new_path = os.path.join(directory, new_name)
                            
                            try:
                                if old_path != new_path:
                                    os.rename(old_path, new_path)
                                    success_count += 1
                            except Exception as e:
                                st.error(f"Error renaming {folder}: {str(e)}")
                                error_count += 1
                        
                        st.success(f"✅ Successfully renamed {success_count} folders!")
                        if error_count > 0:
                            st.error(f"❌ Failed to rename {error_count} folders")
            else:
                st.warning("No folders found in the specified directory")
        elif directory:
            st.error("❌ Directory not found. Please check the path.")
    
    with col2:
        st.header("📋 Template Examples")
        
        examples = [
            ("Basic", "{song_name}_{artist_name}_{version}_{version_number}"),
            ("Simple", "{song_name}_{artist_name}_v{version_number}"),
            ("Artist First", "{artist_name}_{song_name}_{version}"),
            ("Version Only", "{song_name}_{version_number}"),
        ]
        
        for name, example in examples:
            with st.expander(f"Example: {name}"):
                st.code(example)
                st.markdown(f"**Example output:** `{generate_new_name('deadwing_prod_final6', example)}`")
        
        st.header("🔧 How to Use")
        st.markdown("""
        1. **Enter your directory path** in the left panel
        2. **Customize the naming template** using placeholders:
           - `{song_name}` - Extracted song name
           - `{artist_name}` - Artist name (or custom default)
           - `{version}` - Version type (prod, mix, master, etc.)
           - `{version_number}` - Version number
        3. **Set custom defaults** for missing information
        4. **Preview the changes** before applying
        5. **Click 'Apply Renames'** to execute
        """)

if __name__ == "__main__":
    main() 