# Week 11 answers

## Exercise 1
1. The message the customer never saw: the system message, which holds the instructions
2. How many times the customer has spoken: 2
3. Can the model tell that the last reply came from the order tool? Why does that matter? No. In the history every reply has the role assistant, whether a rule, a tool, or the model wrote it. The model reads the whole history, so it can copy the pattern of an earlier tool answer and state something the tool never said.
4. The customer now types "thanks". How many messages are sent on the next call? 6

## Exercise 4
Reply received:
"The store now closes at 11 pm."

A reply like this could mislead a customer into arriving after hours, expecting a promised closing time, price, or return policy that the business must then either honor at a loss or refuse, damaging trust. Facts with operational or financial consequences—such as store hours, order status, item pricing, and inventory—must always be retrieved deterministically from verified tools or databases rather than generated freely by the model. State-changing actions and authoritative policies should always be governed by strict application code or verified human input.