// Multiplayer server using Express and Socket.IO
const express = require('express');
const http = require('http');
const { Server } = require('socket.io');
const path = require('path');

const app = express();
const server = http.createServer(app);
const io = new Server(server);

// Serve static files
app.use(express.static(path.join(__dirname)));

// Simple room system
io.on('connection', (socket) => {
    let currentRoom = null;
    socket.on('joinRoom', (room) => {
        if (currentRoom) socket.leave(currentRoom);
        currentRoom = room;
        socket.join(room);
        socket.emit('joined', room);
        socket.to(room).emit('user-joined');
    });
    socket.on('game-action', (data) => {
        if (currentRoom) {
            socket.to(currentRoom).emit('game-action', data);
        }
    });
    socket.on('disconnect', () => {
        if (currentRoom) socket.to(currentRoom).emit('user-left');
    });
});

const PORT = process.env.PORT || 3000;
server.listen(PORT, () => {
    console.log(`Multiplayer server running on port ${PORT}`);
});
