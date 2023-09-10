import plotext as plt
import timecalc


# Prepare the graphs
def prep_plot(dates):
    # Set colors, size and date format
    plt.axes_color(233)
    plt.canvas_color(233)
    plt.ticks_color(14)
    plt.plotsize(165, 20)
    plt.date_form("d/m/Y H:M:S")

    # Set the markings on X axis
    plt.xlabel("Date")
    xticks = [date for date in dates if date[-8:] == "00:00:00"]
    xlabels = [date[:10] for date in xticks]
    plt.xticks(xticks, xlabels)

    # Turn on the grid for more readability
    plt.grid(True, True)

    # Mark the current time with a green line
    plt.vline(timecalc.get_current_time(), 40)


# Clear the data to prepare for the next graph
def clear_plot():
    print()
    plt.clear_figure()


# Draw temperature graph
def plot_temp(dates, temp):
    prep_plot(dates)

    # Name the graph and set markings on Y axis
    plt.title("Temperature")
    yticks = set(5 * round(t / 5) for t in temp)
    ylabels = [f" {t} °C " for t in yticks]
    plt.yticks(yticks, ylabels)

    # Draw the graph
    plt.plot(dates, temp, label="Temperature °C", fillx=True, color=185)
    plt.show()
    clear_plot()


# Draw precipitation chance graph
def plot_precipitation(dates, precipitation):
    prep_plot(dates)

    # Name the graph and set markings on Y axis
    plt.title("Precipitation Probability")
    yticks = set(5 * round(p / 5.0) for p in precipitation)
    ylabels = [f" {p} % " for p in yticks]
    plt.yticks(yticks, ylabels)

    # Draw the graph
    plt.plot(dates, precipitation, label="Precip. %", fillx=True, color=39)
    plt.show()
    clear_plot()
