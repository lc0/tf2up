var dist_updates = {
  "config": {"view": {"width": 400, "height": 300}, "mark": {"tooltip": null}},
  "layer": [
    {
      "mark": "bar",
      "encoding": {
        "tooltip": [
          {"type": "quantitative", "field": "update_count"},
          {"type": "quantitative", "aggregate": "mean", "field": "update_count"}
        ],
        "x": {"type": "quantitative", "field": "update_count"},
        "y": {"type": "quantitative", "aggregate": "count"}
      },
      "title": "Updates for a file"
    },
    {
      "mark": "rule",
      "encoding": {
        "color": {"type": "nominal", "field": "aggregate"},
        "y": {"type": "quantitative", "field": "value"}
      },
      "transform": [
        {
          "aggregate": [
            {"op": "mean", "field": "update_count", "as": "mean"},
            {"op": "median", "field": "update_count", "as": "median"}
          ]
        },
        {"fold": ["mean", "median"], "as": ["aggregate", "value"]}
      ]
    }
  ],
  "data": {"name": "data-97f086965468e799582fb0e6e8d2c654"},
  "height": 300,
  "$schema": "https://vega.github.io/schema/vega-lite/v3.4.0.json",
  "datasets": {
    "data-97f086965468e799582fb0e6e8d2c654": [
      {"update_count": 1},
      {"update_count": 1},
      {"update_count": 2},
      {"update_count": 2},
      {"update_count": 2},
      {"update_count": 2},
      {"update_count": 2},
      {"update_count": 2},
      {"update_count": 2},
      {"update_count": 3},
      {"update_count": 3},
      {"update_count": 3},
      {"update_count": 3},
      {"update_count": 3},
      {"update_count": 4},
      {"update_count": 4},
      {"update_count": 4},
      {"update_count": 4},
      {"update_count": 5},
      {"update_count": 6},
      {"update_count": 6},
      {"update_count": 6},
      {"update_count": 6},
      {"update_count": 6},
      {"update_count": 6},
      {"update_count": 6},
      {"update_count": 6},
      {"update_count": 6},
      {"update_count": 6},
      {"update_count": 8},
      {"update_count": 8},
      {"update_count": 10},
      {"update_count": 10},
      {"update_count": 10},
      {"update_count": 10},
      {"update_count": 12},
      {"update_count": 12},
      {"update_count": 14},
      {"update_count": 16},
      {"update_count": 17},
      {"update_count": 17},
      {"update_count": 18},
      {"update_count": 20},
      {"update_count": 20},
      {"update_count": 20},
      {"update_count": 22},
      {"update_count": 22},
      {"update_count": 22},
      {"update_count": 28},
      {"update_count": 32},
      {"update_count": 34},
      {"update_count": 41},
      {"update_count": 44},
      {"update_count": 44},
      {"update_count": 55},
      {"update_count": 80},
      {"update_count": 120},
      {"update_count": 134},
      {"update_count": 249}
    ]
  }
};