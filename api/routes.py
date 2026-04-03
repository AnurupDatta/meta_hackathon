from fastapi import APIRouter
from env.crop_env import CropEnv
from utils.leaderboard import update_leaderboard, get_leaderboard

router = APIRouter()
envs = {}

@router.get("/")
def home():
    return {"message": "🌱 AgriAgent Arena is running"}

@router.post("/reset")
def reset(session_id: str):
    envs[session_id] = CropEnv()
    return {"observation": envs[session_id].reset()}

@router.post("/step")
def step(session_id: str, action: int):
    env = envs.get(session_id)

    if not env:
        return {"error": "Session not found"}

    obs, reward, done, _ = env.step(action)

    return {"observation": obs, "reward": reward, "done": done}

@router.get("/leaderboard")
def leaderboard():
    return {"leaderboard": get_leaderboard()}