import json, requests
from typing import List, Dict

OLLAMA_URL = "http://localhost:11434/api/generate"
DEFAULT_MODEL = "llama3:8b"

MOOD_HINTS = {
    "cozy": ["relaxing", "low-stress", "wholesome"],
    "competitive": ["pvp", "ranked", "skill ceiling"],
    "story": ["narrative", "characters", "immersion"],
    "horror": ["suspense", "survival-horror"],
    "adventurous": ["exploration", "open world", "questing"],
    "casual": ["short session", "party-friendly"]
}

def _summarize_games(games: List[Dict], limit: int = 20) -> str:
    rows = []
    for g in games[:limit]:
        name = g.get("name", "Unknown")
        genres = ", ".join(g.get("genres", [])) or "unknown"
        meta = g.get("metacritic", "N/A")
        plats = ", ".join(g.get("platforms", [])) if g.get("platforms") else ""
        rows.append(f"- {name} | genres: {genres} | metacritic: {meta} | platforms: {plats}")
    return "\n".join(rows)

def _heuristic_fallback(mood: str, style: str, games: List[Dict], k: int) -> List[Dict]:
    scored = []
    for g in games:
        genres_text = " ".join(g.get("genres", [])).lower()
        style_score = 40 if style and style.lower() in genres_text else 0
        meta = g.get("metacritic") or 0
        score = style_score + int(meta)
        scored.append((score, g))
    scored.sort(key=lambda x: x[0], reverse=True)
    picks = [x[1] for x in scored[:k]] or games[:k]
    out = []
    for p in picks:
        out.append({
            "name": p.get("name", "Unknown"),
            "why": f"Matches {style} style; strong reviews (Metacritic {p.get('metacritic','N/A')}).",
            "short_review": "Good fit for your selected mood based on genre and reception.",
            "fit_score": 60 + (p.get("metacritic") or 0) // 2
        })
    return out

def _format_text(recs: List[Dict], mood: str, style: str) -> str:
    lines = [f"Top {len(recs)} picks for a {mood} mood with {style} style:\n"]
    for r in recs:
        lines.append(f"• {r['name']} — {r['why']}\n  Review: {r['short_review']}  (Fit: {r.get('fit_]()