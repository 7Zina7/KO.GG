from flask import Flask, render_template_string, request, redirect, url_for, session
from flask_socketio import SocketIO, emit, join_room, leave_room
import random

app = Flask(__name__)
app.secret_key = 'lightsoutsecret'
socketio = SocketIO(app)

# --- Lights Out Logic ---
def create_board(size):
    return [[random.choice([0, 1]) for _ in range(size)] for _ in range(size)]

def toggle(board, x, y):
    size = len(board)
    for dx, dy in [(0,0), (0,1), (0,-1), (1,0), (-1,0)]:
        nx, ny = x+dx, y+dy
        if 0 <= nx < size and 0 <= ny < size:
            board[nx][ny] ^= 1

def is_win(board):
    return all(cell == 0 for row in board for cell in row)

# --- Web UI ---
@app.route('/', methods=['GET', 'POST'])
def index():
    size = 5
    if 'board' not in session:
        session['board'] = create_board(size)
    board = session['board']
    msg = ''
    if request.method == 'POST':
        if 'reset' in request.form:
            session['board'] = create_board(size)
            return redirect(url_for('index'))
        else:
            x, y = int(request.form['x']), int(request.form['y'])
            toggle(board, x, y)
            session['board'] = board
            if is_win(board):
                msg = 'You win!'
    return render_template_string('''
    <h2>Lights Out (Web Version)</h2>
    <form method="post">
    <table style="border-collapse:collapse;">
    {% for i, row in enumerate(board) %}
      <tr>
      {% for j, cell in enumerate(row) %}
        <td style="padding:2px;">
          <button name="x" value="{{i}}" type="submit" formaction="?y={{j}}" style="width:32px;height:32px;background:{{'#ffd700' if cell else '#333'}};color:#222;border-radius:6px;border:1px solid #888;">{{'O' if cell else '.'}}</button>
        </td>
      {% endfor %}
      </tr>
    {% endfor %}
    </table>
    <input type="hidden" name="y" id="yinput">
    <button name="reset" value="1">Reset</button>
    </form>
    <p style="color:green;font-weight:bold;">{{msg}}</p>
    <script>
    // Patch to set y value on button click
    document.querySelectorAll('button[name="x"]').forEach(btn => {
      btn.addEventListener('click', function(e) {
        document.getElementById('yinput').value = btn.getAttribute('formaction').split('=')[1];
      });
    });
    </script>
    <p><a href="/cli">Play CLI version</a></p>
    ''', board=board, msg=msg)

@app.route('/cli')
def cli_info():
    return '''<h2>CLI Games</h2>
    <ul>
      <li>Run <code>python3 a/lights_out.py</code> for Lights Out (CLI)</li>
      <li>Run <code>python3 a/sliding_puzzle.py</code> for Sliding Puzzle (CLI)</li>
      <li>Run <code>python3 a/sudoku_mini.py</code> for Sudoku Mini (CLI)</li>
      <li>Run <code>python3 a/memory_match.py</code> for Memory Match (CLI)</li>
      <li>Run <code>python3 a/word_search.py</code> for Word Search (CLI)</li>
      <li>Run <code>python3 a/maze_solver.py</code> for Maze Solver (CLI)</li>
      <li>Run <code>python3 a/nonogram.py</code> for Nonogram (CLI)</li>
      <li>Run <code>python3 a/color_pattern.py</code> for Color Pattern (CLI)</li>
      <li>Run <code>python3 a/simon_says.py</code> for Simon Says (CLI)</li>
      <li>Run <code>python3 a/towers_of_hanoi.py</code> for Towers of Hanoi (CLI)</li>
    </ul>
    <a href="/">Back to web game</a>'''

# --- Multiplayer Lobby and Chat ---
users = {}
rooms = {}

@app.route('/multiplayer')
def multiplayer_lobby():
    return '''<h2>Multiplayer Lobby</h2>
    <div id="chat"></div>
    <input id="username" placeholder="Username"><input id="room" placeholder="Room"><button onclick="joinRoom()">Join</button>
    <input id="msg" placeholder="Message"><button onclick="sendMsg()">Send</button>
    <script src="https://cdn.socket.io/4.7.5/socket.io.min.js"></script>
    <script>
    var socket = io();
    function joinRoom() {
      socket.emit('join', {username: document.getElementById('username').value, room: document.getElementById('room').value});
    }
    function sendMsg() {
      socket.emit('chat', {room: document.getElementById('room').value, msg: document.getElementById('msg').value});
    }
    socket.on('message', function(data) {
      var chat = document.getElementById('chat');
      chat.innerHTML += '<div>' + data.msg + '</div>';
    });
    </script>
    <a href="/">Back to web game</a>'''

@socketio.on('join')
def on_join(data):
    username = data['username']
    room = data['room']
    join_room(room)
    users[request.sid] = {'username': username, 'room': room}
    emit('message', {'msg': f'{username} has joined the room.'}, room=room)

@socketio.on('leave')
def on_leave(data):
    username = data['username']
    room = data['room']
    leave_room(room)
    emit('message', {'msg': f'{username} has left the room.'}, room=room)

@socketio.on('chat')
def on_chat(data):
    room = data['room']
    msg = data['msg']
    username = users.get(request.sid, {}).get('username', 'Unknown')
    emit('message', {'msg': f'{username}: {msg}'}, room=room)

# --- Maze Solver Logic ---
def generate_maze(width=10, height=10):
    maze = [[1 for _ in range(width)] for _ in range(height)]
    stack = [(0, 0)]
    maze[0][0] = 0
    while stack:
        x, y = stack[-1]
        neighbors = []
        for dx, dy in [(-2,0),(2,0),(0,-2),(0,2)]:
            nx, ny = x+dx, y+dy
            if 0 <= nx < width and 0 <= ny < height and maze[ny][nx] == 1:
                neighbors.append((nx, ny))
        if neighbors:
            nx, ny = random.choice(neighbors)
            maze[(y+ny)//2][(x+nx)//2] = 0
            maze[ny][nx] = 0
            stack.append((nx, ny))
        else:
            stack.pop()
    return maze

def solve_maze(maze):
    from collections import deque
    width, height = len(maze[0]), len(maze)
    queue = deque([((0,0), [(0,0)])])
    visited = set([(0,0)])
    while queue:
        (x, y), path = queue.popleft()
        if (x, y) == (width-1, height-1):
            return path
        for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            nx, ny = x+dx, y+dy
            if 0 <= nx < width and 0 <= ny < height and maze[ny][nx] == 0 and (nx, ny) not in visited:
                visited.add((nx, ny))
                queue.append(((nx, ny), path+[(nx, ny)]))
    return None

@app.route('/maze')
def maze_page():
    width, height = 10, 10
    maze = generate_maze(width, height)
    session['maze'] = maze
    return render_template_string('''
    <h2>Maze Solver (Web Version)</h2>
    <table style="border-collapse:collapse;">
    {% for y, row in enumerate(maze) %}
      <tr>
      {% for x, cell in enumerate(row) %}
        <td style="width:20px;height:20px;background:{{'#222' if cell else '#fff'}};border:1px solid #888;"></td>
      {% endfor %}
      </tr>
    {% endfor %}
    </table>
    <form method="post" action="/maze/solve"><button type="submit">Show Solution</button></form>
    <a href="/">Back to menu</a>
    ''', maze=maze)

@app.route('/maze/solve', methods=['POST'])
def maze_solve():
    maze = session.get('maze')
    if not maze:
        return redirect(url_for('maze_page'))
    path = solve_maze(maze)
    return render_template_string('''
    <h2>Maze Solution</h2>
    <table style="border-collapse:collapse;">
    {% for y, row in enumerate(maze) %}
      <tr>
      {% for x, cell in enumerate(row) %}
        {% set in_path = (x, y) in path %}
        <td style="width:20px;height:20px;background:
            {% if in_path %}#0f0{% elif cell %}#222{% else %}#fff{% endif %};border:1px solid #888;"></td>
      {% endfor %}
      </tr>
    {% endfor %}
    </table>
    <a href="/maze">Try another maze</a> | <a href="/">Back to menu</a>
    ''', maze=maze, path=path or [])

# --- Multiplayer Maze Solver ---
@app.route('/maze-multiplayer')
def maze_multiplayer():
    return '''<h2>Maze Solver Multiplayer</h2>
    <div id="maze"></div>
    <button onclick="solve()">Show Solution</button>
    <div id="chat"></div>
    <input id="username" placeholder="Username"><input id="room" placeholder="Room"><button onclick="joinRoom()">Join</button>
    <input id="msg" placeholder="Message"><button onclick="sendMsg()">Send</button>
    <script src="https://cdn.socket.io/4.7.5/socket.io.min.js"></script>
    <script>
    var socket = io();
    var maze = null, path = null;
    function renderMaze() {
      if (!maze) return;
      let html = '<table style="border-collapse:collapse;">';
      for (let y=0; y<maze.length; y++) {
        html += '<tr>';
        for (let x=0; x<maze[0].length; x++) {
          let color = maze[y][x] ? '#222' : '#fff';
          if (path && path.some(([px,py])=>px==x&&py==y)) color = '#0f0';
          html += `<td style="width:20px;height:20px;background:${color};border:1px solid #888;"></td>`;
        }
        html += '</tr>';
      }
      html += '</table>';
      document.getElementById('maze').innerHTML = html;
    }
    function joinRoom() {
      socket.emit('maze-join', {username: document.getElementById('username').value, room: document.getElementById('room').value});
    }
    function sendMsg() {
      socket.emit('chat', {room: document.getElementById('room').value, msg: document.getElementById('msg').value});
    }
    function solve() {
      socket.emit('maze-solve', {room: document.getElementById('room').value});
    }
    socket.on('maze', function(data) { maze = data.maze; path = null; renderMaze(); });
    socket.on('maze-solution', function(data) { path = data.path; renderMaze(); });
    socket.on('message', function(data) { var chat = document.getElementById('chat'); chat.innerHTML += '<div>' + data.msg + '</div>'; });
    </script>
    <a href="/">Back to menu</a>'''

@socketio.on('maze-join')
def maze_join(data):
    room = data['room']
    username = data['username']
    join_room(room)
    # Generate maze for the room if not exists
    if room not in rooms:
        rooms[room] = {'maze': generate_maze(10, 10)}
    emit('maze', {'maze': rooms[room]['maze']}, room=room)
    emit('message', {'msg': f'{username} joined maze room {room}.'}, room=room)

@socketio.on('maze-solve')
def maze_solve_multiplayer(data):
    room = data['room']
    maze = rooms.get(room, {}).get('maze')
    if maze:
        path = solve_maze(maze)
        emit('maze-solution', {'path': path or []}, room=room)

@app.route('/games')
def games_menu():
    return render_template_string('''
    <h2>Select a Game</h2>
    <div style="display:flex;flex-wrap:wrap;gap:20px;max-width:700px;">
      <button class="game-btn" onclick="window.location='/';">Lights Out</button>
      <button class="game-btn" onclick="window.location='/maze';">Maze Solver</button>
      <button class="game-btn" onclick="window.location='/maze-multiplayer';">Maze Multiplayer</button>
      <button class="game-btn" onclick="window.location='/cli';">CLI Games</button>
      <!-- Add more buttons for other games as web UIs are implemented -->
    </div>
    <style>
      .game-btn {
        font-size: 1.3em;
        padding: 30px 40px;
        border-radius: 12px;
        border: 2px solid #444;
        background: #f5f5f5;
        margin: 10px;
        cursor: pointer;
        transition: background 0.2s, box-shadow 0.2s;
        box-shadow: 2px 2px 8px #bbb;
      }
      .game-btn:hover {
        background: #ffe066;
        box-shadow: 2px 2px 16px #888;
      }
    </style>
    ''')
