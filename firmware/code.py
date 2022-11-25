import time
import array
import math
import board
import audiobusio
import digitalio

# Remove DC bias before computing RMS.
def mean(values):
    return sum(values) / len(values)


def normalized_rms(values):
    minbuf = int(mean(values))
    samples_sum = sum(
        float(sample - minbuf) * (sample - minbuf)
        for sample in values
    )

    return math.sqrt(samples_sum / len(values))


# Main program
# Power on mic
micpwr = digitalio.DigitalInOut(board.MIC_PWR)
micpwr.direction = digitalio.Direction.OUTPUT
micpwr.value = True
time.sleep(0.1)

mic = audiobusio.PDMIn(board.PDM_CLK,board.PDM_DATA,bit_depth=16)
samples = array.array('H', [0] * 160)


while True:
    mic.record(samples, len(samples))
    magnitude = normalized_rms(samples)
    print((magnitude,))
    time.sleep(0.1)