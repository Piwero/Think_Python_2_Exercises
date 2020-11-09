import turtle

def draw(t, length, n):
	
	if n == 0:
		return
	angle= 50
	t.fd(length*n)
	t.lt(angle)
	draw(t, length, n-1)
	t.rt(2*angle)
	draw(t, length, n-1)
	t.lt(angle)
	t.bk(length*n)

def koch_curve(t, n):

    if n < 3:
        t.fd(n)
        return
    m = n/3
    koch_curve(t, m)
    t.lt(60)
    koch_curve(t, m)
    t.rt(120)
    koch_curve(t, m)
    t.lt(60)
    koch_curve(t, m)

def snowflake_koch(t,n):
	for i in range(3):
		koch_curve(t, n)
		t.rt(120)





bob = turtle.Turtle()
bob.fd(-100)
draw(bob, 20, 5)
bob.fd(100)
koch_curve(bob, 20)
bob.fd(100)
snowflake_koch(bob, 300)
turtle.mainloop()
