chrome-ad-detection-list
========================

Chrome has internal histogram metrics to watch when extensions might be injecting ads:

    ExtensionActivity.AdInjected
    ExtensionActivity.AdLikelyInjected
    ExtensionActivity.AdLikelyReplaced
    ExtensionActivity.AdRemoved
    ExtensionActivity.AdReplaced

There's also a subgroup of these just for Google properties:

    ExtensionActivity.Google.AdInjected
    ... etc.
    

These histograms work through the internal chrome extension "activity_log" which calls `IsAdNetwork()` to test URLs when the page source is changed (see `extensions/activity_log/activity_actions.cc`)
