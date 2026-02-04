 
def process_user_data(name, age, email, phone, address, city, state, zip_code, country, is_active, role, department):                
      # Duplicate code blocks                                                                                                          
      if role == "admin":                                                                                                              
          print("Processing admin user")                                    
          result = {}
          result["name"] = name
          result["age"] = age
          result["email"] = email
          result["phone"] = phone
          result["address"] = address
          result["city"] = city
          result["state"] = state
          result["zip_code"] = zip_code
          result["country"] = country
          result["is_active"] = is_active
          result["role"] = role
          result["department"] = department
          result["access_level"] = "full"
      elif role == "manager":
          print("Processing manager user")
          result = {}
          result["name"] = name
          result["age"] = age
          result["email"] = email
          result["phone"] = phone
          result["address"] = address
          result["city"] = city
          result["state"] = state
          result["zip_code"] = zip_code
          result["country"] = country
          result["is_active"] = is_active
          result["role"] = role
          result["department"] = department
          result["access_level"] = "partial"
      elif role == "user":
          print("Processing regular user")
          result = {}
          result["name"] = name
          result["age"] = age
          result["email"] = email
          result["phone"] = phone
          result["address"] = address
          result["city"] = city
          result["state"] = state
          result["zip_code"] = zip_code
          result["country"] = country
          result["is_active"] = is_active
          result["role"] = role
          result["department"] = department
          result["access_level"] = "limited"
      return result

