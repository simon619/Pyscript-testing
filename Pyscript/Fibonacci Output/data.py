def fibo1(n):
    length = n + 1  # Index of the list is positive natural number
    y_plot = [0] * length
    y_plot[1] = y_plot[2] = 1
    for i in range(3, len(y_plot)):
        y_plot[i] = y_plot[i - 1] + y_plot[i - 2]

    y_plot.pop(0)
    x_plot = []
    for i in range(n):
        x_plot.append(i + 1)
    return y_plot[len(y_plot) - 1], x_plot, y_plot  # Time complexity in Linear
