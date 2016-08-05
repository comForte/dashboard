# Dashboard

Quick demo to extract values from log files on NonStop systems
and display them in a dashboard

Uses JavaScript code from dashing.io, batman.js, and jquery.

# Copyright and license

Copyright 2016 - comForte 21 GmbH.
Distributed under the [MIT license](MIT-LICENSE)

# Supported web browsers

The dashboard works with recent firefox, chrome, and Safari browsers.  IE
and Edge are not supported.


# Configuration

Edit index.html to define the widgets in the grid, and then generate the
json to feed each widget with the appropriate values in server.py.
In config.js you can set the update interval.

# Example: Meter widget

```html
<li data-row="1" data-col="1" data-sizex="1" data-sizey="1">
  <div data-id="ssh-sessions" data-view="Meter" data-title="SSH sessions in the last hour" data-min="0" data-max="100"></div>
</li>
```

```json
{"id":"ssh-sessions","value":13,"updatedAt":1470372116}
```

# Example: Number widget

```html
<li data-row="1" data-col="1" data-sizex="1" data-sizey="1">
      <div data-id="puts" data-view="Number" data-title="Puts" data-moreinfo="In millions"></div>
    </li>
```

```json
{"current":2,"id":"puts","updatedAt":1470372116}
```

# Example: Graph widget

```html
  <li data-row="1" data-col="1" data-sizex="2" data-sizey="1">
      <div data-id="remote-ip-addresses" data-view="Graph" data-title="Remote IP Addresses" style="background-color:#ff9618"></div>
    </li>
```

```json
{"points":[{"y":3,"x":0},{"y":25,"x":1},{"y":45,"x":2},{"y":47,"x":3},{"y":40,"x":4},{"y":9,"x":5},{"y":24,"x":6},{"y":27,"x":7},{"y":12,"x":8},{"y":45,"x":9}],"id":"remote-ip-addresses","updatedAt":1470372116}
```

