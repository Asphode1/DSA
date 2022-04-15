var ks = [10, 20, 20, 30, 40]
var ns = [20, 35, 40, 50, 60]

function dequyC(k, n) {
	if (k == 1) return n
	else if (k == n) return 1
	else return dequyC(k, n - 1) + dequyC(k - 1, n - 1)
}

for (let i = 0; i < 5; i++) {
	var start = performance.now()
	dequyC(ks[i], ns[i])
	var end = performance.now()
	console.log(end - start)
}
