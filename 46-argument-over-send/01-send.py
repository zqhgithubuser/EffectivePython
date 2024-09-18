import math


# amplitude: 波的振幅
# steps: 将一个完整的周期（2π 弧度）划分为 steps 步
def wave_modulating(steps):
    step_size = 2 * math.pi / steps
    amplitude = yield  # 初始振幅
    for step in range(steps):
        radians = step * step_size
        fraction = math.sin(radians)
        output = amplitude * fraction
        amplitude = yield output  # 接收新的振幅


def transmit(output):
    if output is None:
        print("Output is None")
    else:
        print(f"Output: {output:>5.1f}")


def run_modulating(it):
    amplitudes = [None, 7, 7, 7, 2, 2, 2, 2, 10, 10, 10, 10, 10]
    # 不同振幅
    for amplitude in amplitudes:
        output = it.send(amplitude)
        transmit(output)


def complex_wave_modulating():
    yield from wave_modulating(3)
    yield from wave_modulating(4)
    yield from wave_modulating(5)


# run_modulating(wave_modulating(12))

run_modulating(complex_wave_modulating())
