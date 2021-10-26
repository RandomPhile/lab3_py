import sympy as sp

x, a, V_0, E = sp.symbols('x a V_0 E')

V = sp.Piecewise(
	(0   , x<-a),
	(0   , x>a),
	(-V_0, True)
)

print(V.subs([(x,1), (a, 0.5)]))