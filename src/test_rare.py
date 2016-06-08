
from nose.tools import assert_equal, assert_almost_equal, assert_true, \
    assert_false, assert_raises, assert_is_instance
import numpy as np
from subprocess import call
from numpy import array

from rare import fract, calc_resampled_fraction, plotme

FIXTURE = np.array([[100, 1000]], dtype="float")
FIXTURE2 = np.array([[1,1000], [10,1000], [100, 1000]], dtype="float")

# fract(aa, epsilon, threshold)
def test_calccumsum_one_full():
    data = np.array([[100, 1000]], dtype="float")
    result = fract(data, 1, 1)
    assert_equal(result, 1)
    result2 = fract(FIXTURE2, 1, 1)
    assert_equal(result, 1)
    result3 = fract(FIXTURE2, .5, 1)

def test_calccumsum_one_zero():
    data = np.array([[100, 1000]], dtype="float")
    result = fract(data, 1, 100000)
    assert_equal(result, 0)

def test_calccumsum_one_half():
    data = np.array([[100, 1000]], dtype="float")
    result = fract(data, 0.5, 50)
    print result
    assert_true(result > 0.3)
    assert_true(result < 0.7)

def test_calccumsum_two_full():
    data = np.array([[100, 1000], [20000, 10000]], dtype="float")
    result = fract(data, 1, 1)
    assert_equal(result, 1)

def test_calccumsum_two_zero():
    data = np.array([[100, 1000], [20000, 10000]], dtype="float")
    result = fract(data, 1, 100000)
    assert_equal(result, 0)

def test_calccumsum_two_tenth():
    data = np.array([[100, 1000], [1000, 1000]], dtype="float")
    result = fract(data, 1, 200)
    assert_true(result > 0.88)
    assert_true(result < 0.92)

def test_calc_resampled_fraction():
    samplefracs = np.array([[.01, .03, .1, .3]]).T
    thresholds = np.array([[1,3,10,30,100]]).T
    m = calc_resampled_fraction(FIXTURE, samplefracs, thresholds)
    print m.shape 
    assert_true(m.shape[0] == len(samplefracs))
    assert_true(m.shape[1] == len(thresholds))
    m2 = calc_resampled_fraction(FIXTURE2, samplefracs, thresholds)
    assert_true(m2.shape[0] == len(samplefracs))
    assert_true(m2.shape[1] == len(thresholds))

def test_plotme0():
    p = plotme(FIXTURE, "templabel", shaded=0)
    p = plotme(FIXTURE2, "templabel", shaded=0)
def test_plotme1():
    p = plotme(FIXTURE, "templabel", shaded=1)
    p = plotme(FIXTURE2, "templabel", shaded=1)
def test_plotme2():
    p = plotme(FIXTURE, "templabel", shaded=2)
    p = plotme(FIXTURE2, "templabel", shaded=2)
def test_plotme3():
    p = plotme(FIXTURE, "templabel", shaded=3)
    p = plotme(FIXTURE2, "templabel", shaded=3)
def test_plotmeS():
    p = plotme(FIXTURE, "templabel", shaded=2, suppress=True)
    p = plotme(FIXTURE2, "templabel", shaded=2, suppress=True)
def test_plotmeD():
    p = plotme(FIXTURE, "templabel", shaded=2, dump=True)
    p = plotme(FIXTURE2, "templabel", shaded=2, dump=True)

def test_plotmeT():
    p = plotme(FIXTURE, "templabel", shaded=2, thresholdlist=[1,10,100])
    p = plotme(FIXTURE2, "templabel", shaded=2, thresholdlist=[1,10,100])

def test_cmdline1():
    call("rare.py -g 2 ../repeatresolutionpaper/counts-validationgenomedata/list -s -o list.rare.2s.png", shell=True)
    call("rare.py -g 2 ../repeatresolutionpaper/counts-validationgenomedata/list -o list.rare.2s.png", shell=True)

def test_cmdline2():
    call("stratify.py -l ../repeatresolutionpaper/counts-validationgenomedata/list  -g 0 -o list.frac3.pdf", shell=True)
    call("stratify.py -l ../repeatresolutionpaper/counts-validationgenomedata/list  -g 1 -o list.size3.pdf", shell=True)
    call("stratify.py -l ../repeatresolutionpaper/counts-validationgenomedata/list  -g 0 -s -o list.frac3s.pdf", shell=True)
    call("stratify.py -l ../repeatresolutionpaper/counts-validationgenomedata/list  -g 1 -s -o list.size3s.pdf", shell=True)


