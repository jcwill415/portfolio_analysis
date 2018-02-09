import datetime

from portfolio_creator.data_source import DataSource
from portfolio_creator.portfolio_creator import PortfolioCreator
from pylab import plot, xlabel, ylabel, title, show
from utilities.constants import Constants
from utilities.epoch_date_converter import EpochDateConverter

portfolio = PortfolioCreator().create(DataSource())
number_of_days = Constants.DAYS_PER_YEAR * 15

times = []
owners_equity = []

for day in range(0, number_of_days):
    historical_time = EpochDateConverter().date_to_epoch() - day * Constants.SECONDS_PER_DAY
    formatted_date = EpochDateConverter().epoch_to_date(historical_time)
    times.append(datetime.datetime.fromtimestamp(historical_time))
    owners_equity.append(portfolio.total_value(formatted_date))

plot(times, owners_equity)
xlabel('Date')
ylabel("Owner's Equity")
title("Owner's Equity vs. Time")
show()