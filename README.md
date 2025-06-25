# Archive Producer Batch Renamer

A modern web application for renaming music production project folders with consistent naming conventions.

## Features

- 🎵 **Smart Pattern Recognition** - Automatically extracts song names, artist names, and version information
- 📁 **Batch Processing** - Rename multiple folders at once
- 👀 **Preview Mode** - See changes before applying them
- 🎨 **Custom Templates** - Define your own naming patterns
- 🔧 **Custom Mappings** - Set default values for missing information
- 🛡️ **Safe Operations** - Preview all changes before execution

## Setup

### 1. Create Virtual Environment

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On macOS/Linux:
source venv/bin/activate
# On Windows:
venv\Scripts\activate
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the Application

```bash
streamlit run app.py
```

The application will open in your default web browser at `http://localhost:8501`

## Usage

1. **Enter Directory Path** - Specify the folder containing your music projects
2. **Customize Template** - Use placeholders like `{song_name}`, `{artist_name}`, `{version}`, `{version_number}`
3. **Set Defaults** - Provide default values for missing information
4. **Preview Changes** - Review what will be renamed before applying
5. **Apply Renames** - Execute the batch rename operation

## Example Templates

- `{song_name}_{artist_name}_{version}_{version_number}` → `deadwing_porcupine_tree_prod_6`
- `{artist_name}_{song_name}_v{version_number}` → `porcupine_tree_deadwing_v6`
- `{song_name}_{version_number}` → `deadwing_6`

## Supported Patterns

The app recognizes common music production naming patterns:

- `prod`, `mix`, `master`, `final`
- Version numbers (`v1`, `v2`, `final6`, etc.)
- Artist names and song titles

## Safety Features

- Preview all changes before execution
- Error handling for failed renames
- No changes made until you click "Apply Renames"
- Detailed feedback on success/failure

## Development

To deactivate the virtual environment when done:

```bash
deactivate
```
