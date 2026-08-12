from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from account import users_database, laptop, phone

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# Պահում ենք ակտիվ օգտատիրոջ անունը (պարզեցված տարբերակով)
current_username = "arman"

@app.get("/login", response_class=HTMLResponse)
async def show_login_form(request: Request):
    return templates.TemplateResponse(request=request, name="login.html")

@app.post("/login", response_class=HTMLResponse)
async def login(request: Request, username: str = Form(...), password: str = Form(...)):
    global current_username
    user = users_database.get(username)

    if user and user.check_password(password):
        current_username = username
        return render_dashboard(request, user)
    
    return templates.TemplateResponse(
        request=request, 
        name="login.html", 
        context={"error": "Սխալ օգտանուն կամ գաղտնաբառ:"}
    )

# 1․ ԿՈՃԱԿՈՎ ԱՊՐԱՆՔ ԱՎԵԼԱՑՆԵԼՈՒ ՖՈՒՆԿՑԻԱ
@app.post("/add-to-cart", response_class=HTMLResponse)
async def add_to_cart(request: Request, item_name: str = Form(...)):
    user = users_database.get(current_username)
    if user:
        if item_name == "laptop":
            user.cart.add_product(laptop, 1)
        elif item_name == "phone":
            user.cart.add_product(phone, 1)
    return render_dashboard(request, user)

# 2․ ԿՈՃԱԿՈՎ ԱՊՐԱՆՔ ՋՆՋԵԼՈՒ ՖՈՒՆԿՑԻԱ
@app.post("/remove-from-cart", response_class=HTMLResponse)
async def remove_from_cart(request: Request, item_name: str = Form(...)):
    user = users_database.get(current_username)
    if user:
        if item_name == "laptop":
            user.cart.remove_product(laptop, 1)
        elif item_name == "phone":
            user.cart.remove_product(phone, 1)
    return render_dashboard(request, user)

# Oգնական ֆունկցիա էջը ցույց տալու համար
def render_dashboard(request: Request, user):
    return templates.TemplateResponse(
        request=request, 
        name="dashboard.html", 
        context={
            "username": user.username,
            "balance": user.balance,
            "cart_items": user.cart.items,
            "cart_total": user.cart.get_total(),
            "laptop_stock": laptop.stock,
            "phone_stock": phone.stock
        }
    )