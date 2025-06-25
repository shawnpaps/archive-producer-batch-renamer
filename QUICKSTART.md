# Quick Start Guide

## 🚀 Get Started in 3 Steps

### Option 1: Automated Setup (Recommended)

**macOS/Linux:**

```bash
./setup.sh
```

**Windows:**

```cmd
setup.bat
```

### Option 2: Manual Setup

1. **Create and activate virtual environment:**

   ```bash
   python -m venv venv
   source venv/bin/activate  # macOS/Linux
   # or
   venv\Scripts\activate     # Windows
   ```

2. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the app:**
   ```bash
   streamlit run app.py
   ```

## 🎯 First Use

1. Open your browser to `http://localhost:8501`
2. Enter the path to your music projects folder
3. Try the default template: `{song_name}_{artist_name}_{version}_{version_number}`
4. Preview the changes
5. Click "Apply Renames" when satisfied

## 📁 Example

**Before:**

```
deadwing_prod_final6/
sicknastysong_turnpikesouth_prod1/
```

**After (with template `{song_name}_{artist_name}_{version}_{version_number}`):**

```
deadwing_porcupine_tree_prod_6/
sicknastysong_turnpikesouth_prod_1/
```

## 🛡️ Safety Features

- ✅ Preview all changes before applying
- ✅ No changes made until you confirm
- ✅ Error handling for failed operations
- ✅ Detailed success/failure feedback

## 🆘 Need Help?

- Check the main README.md for detailed documentation
- The app includes built-in examples and help text
- All operations are previewed before execution
