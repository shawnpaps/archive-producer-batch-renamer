#!/bin/bash

echo "🎵 Starting Archive Producer Batch Renamer..."

# Activate virtual environment
source venv/bin/activate

# Start Streamlit
echo "🚀 Launching Streamlit app..."
streamlit run app.py --server.headless=true --server.port=8501 &

# Wait for Streamlit to start
echo "⏳ Waiting for Streamlit to start..."
sleep 5

# Check if Streamlit is running
if curl -s http://localhost:8501 > /dev/null; then
    echo "✅ Streamlit is running at http://localhost:8501"
    echo "🌐 Open your browser to http://localhost:8501"
    echo ""
    echo "Press Ctrl+C to stop the app"
    
    # Keep the script running
    wait
else
    echo "❌ Failed to start Streamlit"
    exit 1
fi 