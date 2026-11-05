#!/bin/bash
# 내 화면에서만 보는 실행 (밖으로 공개되지 않음). 중지: ./run.sh stop
cd "$(dirname "$0")"
if [ "$1" = stop ]; then kill "$(cat server.pid 2>/dev/null)" 2>/dev/null; rm -f server.pid; exit 0; fi
[ -f server.pid ] && kill "$(cat server.pid)" 2>/dev/null
setsid nohup python3 -m uvicorn main:app --host 127.0.0.1 --port 8000 > server.log 2>&1 &
echo $! > server.pid
