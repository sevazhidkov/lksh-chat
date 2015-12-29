from app import socketio, app

socketio.run(app, debug=True, port=80, host='0.0.0.0')
