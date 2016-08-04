var updateIntervalSeconds = 60

function setupDataUpdater(dashingListeners) {
  function update() {
    return jQuery.ajax({
      url: "/data",
      type: "GET",
      success: function(response) {
        var a = response
        a.forEach(function(m) { dashingListeners.callbacks.message(m) })
      }
    })
  }
  update()
  setInterval(function() { update() }, updateIntervalSeconds*1000)
}
