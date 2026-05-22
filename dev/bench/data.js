window.BENCHMARK_DATA = {
  "lastUpdate": 1779435227688,
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
      },
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
          "id": "d0313942f5bc6dc1ca613c3b1dc5068021b1832e",
          "message": "Poprawia wersje actions",
          "timestamp": "2026-05-22T09:32:43+02:00",
          "tree_id": "e9a7a017fae2bdb2c2a58d32c809bd63a4a1bce0",
          "url": "https://github.com/DanielMierzwa/OOB_Tests-ImageIO/commit/d0313942f5bc6dc1ca613c3b1dc5068021b1832e"
        },
        "date": 1779435226859,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/performance/test_compression.py::test_png_compression_high_level",
            "value": 3.592131043825667,
            "unit": "iter/sec",
            "range": "stddev: 0.002144650461987186",
            "extra": "mean: 278.3862804000009 msec\nrounds: 5"
          },
          {
            "name": "tests/performance/test_compression.py::test_tiff_lossless_compression",
            "value": 151.74488686408614,
            "unit": "iter/sec",
            "range": "stddev: 0.009897025502576061",
            "extra": "mean: 6.5900078787872 msec\nrounds: 33"
          },
          {
            "name": "tests/performance/test_load_time.py::test_load_time",
            "value": 47.00356955148732,
            "unit": "iter/sec",
            "range": "stddev: 0.00021147325585806965",
            "extra": "mean: 21.27497995454597 msec\nrounds: 44"
          }
        ]
      }
    ]
  }
}