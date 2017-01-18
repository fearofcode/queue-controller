import random

class Buffer(object):
    def __init__(self, max_ready, max_flow):
        self.queued = 0
        self.ready = 0

        self.max_ready = max_ready
        self.max_flow = max_flow

    def work(self, process_input):
        additional_ready = max(0, int(round(process_input)))
        additional_ready = min(additional_ready, self.max_ready)
        # add to ready pool
        self.ready += additional_ready

        # transfer from ready pool to queue
        ready_flow = int(round(random.uniform(0, self.ready)))
        self.ready -= ready_flow
        self.queued += ready_flow

        # queue -> downstream
        downstream_flow = int(round(random.uniform(0, self.max_flow)))
        downstream_flow = min(downstream_flow, self.queued)
        self.queued -= downstream_flow

        return self.queued


class Controller(object):
    def __init__(self, proportional_gain, integral_gain):
        self.proportional_gain = proportional_gain
        self.integral_gain = integral_gain

        self.cumulative_error = 0

    def work(self, error):
        self.cumulative_error += error

        return self.proportional_gain * error + self.integral_gain * self.cumulative_error


def setpoint(t):
    if t < 100:
        return 0
    elif t < 300:
        return 50

    return 10


if __name__ == "__main__":
    controller = Controller(1.25, 0.01)
    process = Buffer(50, 10)

    time_steps = 1000
    process_output = 0

    for t in range(time_steps):
        current_setpoint = setpoint(t)
        error = current_setpoint - process_output
        controller_input = controller.work(error)
        process_output = process.work(controller_input)

        print(t, current_setpoint, error, controller_input, process_output)
