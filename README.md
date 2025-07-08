# Archive Producer Batch Renamer

A desktop application for batch renaming music production folders with consistent naming conventions.

## Features

- 🎵 Batch rename music production folders
- 📝 Custom naming templates with placeholders
- 👀 Preview changes before applying
- 🎨 Modern, intuitive interface
- 💻 Cross-platform desktop application

## Installation

### For End Users (Producers/Engineers)

1. **Download the latest release** for your platform:

   - macOS: `.dmg` file
   - Windows: `.exe` installer
   - Linux: `.AppImage` file

2. **Install and run** the application

### For Developers

1. **Clone the repository**

   ```bash
   git clone <repository-url>
   cd archive-producer-batch-renamer
   ```

2. **Install Python dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Install Node.js dependencies**

   ```bash
   npm install
   ```

4. **Run in development mode**
   ```bash
   npm run dev
   ```

## Building for Distribution

### Prerequisites

- Python 3.8+
- Node.js 16+
- npm

### Build Steps

1. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   npm install
   ```

2. **Build the desktop app**

   ```bash
   npm run build
   ```

3. **Find the built app** in the `dist/` folder

## Usage

1. **Launch the application**
2. **Enter your music projects directory path**
3. **Customize the naming template** using placeholders:
   - `{song_name}` - Extracted song name
   - `{artist_name}` - Artist name
   - `{version}` - Version type (prod, mix, master, etc.)
   - `{version_number}` - Version number
4. **Set custom defaults** for missing information
5. **Preview the changes** before applying
6. **Click 'Apply Renames'** to execute

## Template Examples

- **Basic**: `{song_name}_{artist_name}_{version}_{version_number}`
- **Simple**: `{song_name}_{artist_name}_v{version_number}`
- **Artist First**: `{artist_name}_{song_name}_{version}`
- **Version Only**: `{song_name}_{version_number}`

## Development

### Project Structure

```
├── app.py              # Main Streamlit application
├── main.js             # Electron main process
├── package.json        # Node.js dependencies and build config
├── requirements.txt    # Python dependencies
└── .streamlit/         # Streamlit configuration
```

### Running Tests

```bash
# Add tests when implemented
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

[Add your license here]

## Support

For issues and questions, please open an issue on GitHub.
