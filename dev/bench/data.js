window.BENCHMARK_DATA = {
  "lastUpdate": 1779433455815,
  "repoUrl": "https://github.com/DanielMierzwa/OOB_Tests-ImageIO",
  "entries": {
    "Benchmark": [
      {
        "commit": {
          "author": {
            "email": "rospondek.szymon@gmail.com",
            "name": "Szymon"
          },
          "committer": {
            "email": "rospondek.szymon@gmail.com",
            "name": "Szymon"
          },
          "distinct": true,
          "id": "0a0d81057641b009a27484fbcefd62d25478772e",
          "message": "Dodaje workflow_dispatch z powrotem do pipeline",
          "timestamp": "2026-05-22T08:57:48+02:00",
          "tree_id": "c8e6e8ea57b8208cb974c79aa4d77e766fdf1bc2",
          "url": "https://github.com/DanielMierzwa/OOB_Tests-ImageIO/commit/0a0d81057641b009a27484fbcefd62d25478772e"
        },
        "date": 1779433455480,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/performance/test_compression.py::test_png_compression_high_level",
            "value": 3.692587993594594,
            "unit": "iter/sec",
            "range": "stddev: 0.0011767461110082885",
            "extra": "mean: 270.81277460000024 msec\nrounds: 5"
          },
          {
            "name": "tests/performance/test_compression.py::test_tiff_lossless_compression",
            "value": 291.710487183499,
            "unit": "iter/sec",
            "range": "stddev: 0.0002897750373039072",
            "extra": "mean: 3.4280563913046946 msec\nrounds: 23"
          },
          {
            "name": "tests/performance/test_load_time.py::test_load_time",
            "value": 57.876799761350746,
            "unit": "iter/sec",
            "range": "stddev: 0.00067872961657641",
            "extra": "mean: 17.278080407406787 msec\nrounds: 54"
          }
        ]
      }
    ]
  }
}