#!/bin/bash
set -e

GREEN='\033[0;32m'
NC='\033[0m' # No Color

echo -e "${GREEN}Activating virtual environment...${NC}"
source venv/bin/activate

echo -e "${GREEN}Installing dependencies...${NC}"
pip install -r requirements.txt

mkdir -p logs

echo -e "${GREEN}Starting Prefect Orion server...${NC}"
prefect server start > logs/prefect_server.log 2>&1 & SERVER_PID=$!

sleep 5


echo -e "${GREEN}Starting Prefect agent...${NC}"
prefect agent start -q default > logs/prefect_agent.log 2>&1 & AGENT_PID=$!

sleep 5

echo -e "${GREEN}Starting the flow...${NC}"
python3 start_flow.py > logs/flow_run.log 2>&1 & FLOW_PID=$!


echo -e "${GREEN} Running flow...${NC}"
echo "Server PID: $SERVER_PID"
echo "Agent PID: $AGENT_PID"
echo "Flow PID: $FLOW_PID"


trap "echo -e '${GREEN}Stopping all processes...${NC}'; kill $SERVER_PID $AGENT_PID $FLOW_PID; exit" SIGINT SIGTERM

wait