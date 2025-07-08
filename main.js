const { app, BrowserWindow, Menu } = require('electron');
const path = require('path');
const { spawn } = require('child_process');

let mainWindow;
let streamlitProcess;

function createWindow() {
	mainWindow = new BrowserWindow({
		width: 1200,
		height: 800,
		webPreferences: {
			nodeIntegration: false,
			contextIsolation: true,
		},
		title: 'Archive Producer Batch Renamer',
		icon: path.join(__dirname, 'icon.png'), // Add an icon if you have one
		show: false, // Don't show until ready
	});

	// Load the Streamlit app
	mainWindow.loadURL('http://localhost:8501');

	// Show window when ready
	mainWindow.once('ready-to-show', () => {
		mainWindow.show();
	});

	// Create menu
	const template = [
		{
			label: 'File',
			submenu: [
				{
					label: 'Quit',
					accelerator: process.platform === 'darwin' ? 'Cmd+Q' : 'Ctrl+Q',
					click: () => {
						app.quit();
					},
				},
			],
		},
		{
			label: 'View',
			submenu: [
				{ role: 'reload' },
				{ role: 'forceReload' },
				{ role: 'toggleDevTools' },
				{ type: 'separator' },
				{ role: 'resetZoom' },
				{ role: 'zoomIn' },
				{ role: 'zoomOut' },
				{ type: 'separator' },
				{ role: 'togglefullscreen' },
			],
		},
	];

	const menu = Menu.buildFromTemplate(template);
	Menu.setApplicationMenu(menu);

	mainWindow.on('closed', () => {
		mainWindow = null;
	});
}

function startStreamlit() {
	// Determine the Python executable path
	const pythonPath =
		process.platform === 'win32'
			? path.join(__dirname, 'venv', 'Scripts', 'python.exe')
			: path.join(__dirname, 'venv', 'bin', 'python');

	// Start Streamlit process
	streamlitProcess = spawn(
		pythonPath,
		[
			'-m',
			'streamlit',
			'run',
			'app.py',
			'--server.port=8501',
			'--server.headless=true',
		],
		{
			stdio: 'pipe',
			cwd: __dirname,
		}
	);

	streamlitProcess.stdout.on('data', (data) => {
		console.log(`Streamlit: ${data}`);
	});

	streamlitProcess.stderr.on('data', (data) => {
		console.error(`Streamlit Error: ${data}`);
	});

	streamlitProcess.on('error', (error) => {
		console.error(`Failed to start Streamlit: ${error}`);
	});
}

app.whenReady().then(() => {
	startStreamlit();

	// Wait a bit for Streamlit to start
	setTimeout(() => {
		createWindow();
	}, 3000);

	app.on('activate', () => {
		if (BrowserWindow.getAllWindows().length === 0) {
			createWindow();
		}
	});
});

app.on('window-all-closed', () => {
	if (process.platform !== 'darwin') {
		app.quit();
	}
});

app.on('before-quit', () => {
	if (streamlitProcess) {
		streamlitProcess.kill();
	}
});
