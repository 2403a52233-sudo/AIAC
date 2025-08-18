import json, os; F = "users.json"

def register_user(u, p):
    u, p = (u or "").strip(), (p or "").strip(); x = json.load(open(F, "r", encoding="utf-8")) if os.path.exists(F) else {}
    if not u or not p or u in x: return False
    x[u] = p; json.dump(x, open(F, "w", encoding="utf-8"), ensure_ascii=False, indent=2); return True

def login_user(u, p):
    x = json.load(open(F, "r", encoding="utf-8")) if os.path.exists(F) else {}
    return x.get((u or "").strip()) == (p or "").strip()

if __name__ == "__main__":
    c = input("1)Reg 2)Log: ").strip(); u = input("User: ").strip(); p = input("Pass: ").strip()
    print("OK" if (register_user if c == "1" else login_user)(u, p) else "Fail")

