response = supabase.table("test").select("*").execute()
# print(response)