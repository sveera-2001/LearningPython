cost_pgs = 125.0

def ground_shipping(weight):
  if weight<2:
    cost = weight*1.5 + 20
  elif weight>2 and weight<=6:
    cost = weight*3.0 + 20
  elif weight>6 and weight<=10:
    cost = weight*4.0 + 20
  else:
    cost = weight*4.75 + 20
  return cost

def drone_shipping(weight):
  if weight<2:
    cost = weight*4.5
  elif weight>2 and weight<=6:
    cost = weight*9.0
  elif weight>6 and weight<=10:
    cost = weight*12.0
  else:
    cost = weight*14.25
  return cost

def determine(weight):
  if ground_shipping(weight) < drone_shipping(weight) and ground_shipping(weight) < cost_pgs :
    print("Mode of shipping:Ground shipping")
    print("Cost:",ground_shipping(weight))
  elif ground_shipping(weight) > drone_shipping(weight) and drone_shipping(weight) < cost_pgs :
    print("Mode of shipping:Drone shipping")
    print("Cost:",drone_shipping(weight))
  elif cost_pgs < ground_shipping(weight) and cost_pgs < drone_shipping(weight):
    print("Mode of shipping:Premium Ground shipping")
    print("Cost:",cost_pgs)   

determine(4.5)
