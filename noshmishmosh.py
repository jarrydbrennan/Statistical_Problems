import noshmishmosh
import numpy as np

#establishing baseline
all_visitors = noshmishmosh.customer_visits
paying_visitors = noshmishmosh.purchasing_customers
total_visitor_count = len(all_visitors)
paying_visitor_count = len(paying_visitors)

baseline_percent = paying_visitor_count/total_visitor_count * 100
print(baseline_percent)

#average sales per order
payment_history = noshmishmosh.money_spent
average_payment = np.mean(payment_history)

#how many 'usual' payments would it take to clear $1240 mark
new_customers_needed = np.ceil(1240/ average_payment)

#percentage increase of new customers to hit mark
percentage_point_increase = new_customers_needed/total_visitor_count *100
print(percentage_point_increase)

#mde/desired lift
mde = percentage_point_increase/baseline_percent *100
print(mde)

ab_sample_size = 490