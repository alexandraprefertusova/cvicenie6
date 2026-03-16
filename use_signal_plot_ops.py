import signal_plot_ops as sig

values = sig.load_signal_from_txt("ekg_signal.txt")

print("Average:", sig.signal_avg(values))

sig.plot_signal(values)
