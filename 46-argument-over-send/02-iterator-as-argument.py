import math


# amplitude: 波的振幅
# steps: 将一个完整的周期（2π 弧度）划分为 steps 步
def wave_cascading(amplitude_it, steps):
    step_size = 2 * math.pi / steps
    for step in range(steps):
        radians = step * step_size
        fraction = math.sin(radians)
        amplitude = next(amplitude_it)
        output = amplitude * fraction
        yield output


def transmit(output):
    if output is None:
        print("Output is None")
    else:
        print(f"Output: {output:>5.1f}")


def complex_wave_cascading(amplitude_it):
    yield from wave_cascading(amplitude_it, 3)
    yield from wave_cascading(amplitude_it, 4)
    yield from wave_cascading(amplitude_it, 5)


def run_cascading():
    amplitudes = [7, 7, 7, 2, 2, 2, 2, 10, 10, 10, 10, 10]
    it = complex_wave_cascading(iter(amplitudes))
    for i, _ in enumerate(amplitudes):
        output = next(it)
        transmit(output)


run_cascading()
