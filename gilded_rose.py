# -*- coding: utf-8 -*-


class Item:
    """ DO NOT CHANGE THIS CLASS!!!"""
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


class GildedRose(object):

    def __init__(self, items: list[Item]):
        # DO NOT CHANGE THIS ATTRIBUTE!!!
        self.items = items

    def update_quality(self):
        """Update the quality of all items in the store for one day."""
        for item in self.items:
            self.update_item(item)

    def update_item(self, item):
        """Update the quality and sell-in values for a single item."""
        if item.name == "Sulfuras, Hand of Ragnaros":
            return
        self.update_sell_in(item)
        if item.name == "Aged Brie":
            self.update_aged_brie(item)
        elif item.name == "Backstage passes to a TAFKAL80ETC concert":
            self.update_backstage_pass(item)
        else:
            self.update_normal_item(item)
        self.ensure_quality_limits(item)

    def update_sell_in(self, item):
        """Decrease the sell-in value for an item."""
        item.sell_in -= 1

    def update_aged_brie(self, item):
        """Update the quality for 'Aged Brie', which increases in quality over time."""
        self.increase_quality(item)
        if item.sell_in < 0:
            self.increase_quality(item)

    def update_backstage_pass(self, item):
        """Update the quality for 'Backstage passes', which increases as the concert date approaches."""
        self.increase_quality(item)
        if item.sell_in < 10:
            self.increase_quality(item)
        if item.sell_in < 5:
            self.increase_quality(item)
        if item.sell_in < 0:
            item.quality = 0

    def update_normal_item(self, item):
        """Update the quality for normal items, which degrade in quality over time."""
        self.decrease_quality(item)
        if item.sell_in < 0:
            self.decrease_quality(item)

    def increase_quality(self, item):
        """Increase the quality of an item, ensuring it does not go over 50."""
        if item.quality < 50:
            item.quality += 1

    def decrease_quality(self, item):
        """Decrease the quality of an item, ensuring it does not go negative."""
        if item.quality > 0:
            item.quality -= 1

    def ensure_quality_limits(self, item):
        """Ensure an item's quality is within the 0-50 range."""
        item.quality = max(0, min(50, item.quality))