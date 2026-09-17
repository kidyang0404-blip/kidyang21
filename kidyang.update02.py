def gradient(w):
    return 2 * (w - 3)

def gradient_descent(w_init, learning_rate, tolerance, max_iter):
    w = w_init
    history = [w] 
    for t in range(max_iter):
        grad = gradient(w)
        w_next = w -learning_rate * grad  

        history.append(w_next)

        if abs(w_next - w) < tolerance: 
            return w_next, t +1, history
        
        w = w_next

    return (w, max_iter, history)

w_final, steps, history = gradient_descent(w_init=0.0, learning_rate=0.1, tolerance=0.000001, max_iter=100)
print(f"최종 가중치: w = {w_final:.4f}, 총 {steps}회 반복")