# Completed Product example Exercises



### Getting started

**Start by cloning this repository and opening in VS Code.**

1. Configure the Python Virtual Environment

   `python -m venv venv --prompt="products_ex_complete"`

2. Activate the Virtual Environment

   `venv\Scripts\activate`

3. Install dependencies (note addition of `supabase`)

   `pip install fastapi uvicorn jinja2 python-multipart httpx supabase`

4. Setup the `.env` file, e.g. based on `.env.example` - you will need to add your Supabase URL and API Key

5. To run the application

   `uvicorn app.main:app --reload --port=3000`
