# Timeflux

Timeflux is a free and open-source solution for the acquisition and real-time processing of biosignals.
Use it to bootstrap your research, build brain-computer interfaces, closed-loop biofeedback applications, interactive installations, and more. Written in Python, it works on Linux, MacOS and Windows. Made for researchers and hackers alike.

## Installation

First, get the [Anaconda distribution](https://www.anaconda.com/download/).

You can then install Timeflux and its dependencies:

```
$ curl -O https://raw.githubusercontent.com/timeflux/timeflux/master/environment.yml
$ conda env create -f environment.yml
$ conda activate timeflux
```

## Getting started

[Read the documentation](https://doc.timeflux.io).

For a minimal working example:
```
$ curl -O https://raw.githubusercontent.com/timeflux/timeflux/master/test/graphs/test.yaml
$ timeflux test.yaml
```

If you install also [timeflux_ui](https://github.com/timeflux/timeflux_ui), you could run a sample visualization:
```
$ curl -O https://raw.githubusercontent.com/timeflux/timeflux/master/test/graphs/ui.yaml
$ timeflux ui.yaml
```
Once it is launched, you could access it in [your browser](http://0.0.0.0:8000)

More examples of Timeflux graphs are available in [test/graphs](https://github.com/timeflux/timeflux/tree/master/test/graphs)

## Fair warning

This is an early release. Use at your own risk.
