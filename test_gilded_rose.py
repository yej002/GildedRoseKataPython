# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEquals("foo", items[0].name)

    def test_update_quality(self):
        """Test that update_quality correctly updates all items."""
        items = [Item("Normal Item", 5, 10), Item("Aged Brie", 5, 0), Item("Backstage passes", 5, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(items[0].quality, 9)
        self.assertEqual(items[0].sell_in, 4)
        self.assertEqual(items[1].quality, 1)
        self.assertEqual(items[2].quality, 9)

    def test_update_item(self):
        """Test that update_item correctly updates a single item."""
        item = Item("Normal Item", 5, 10)
        gilded_rose = GildedRose([item])
        gilded_rose.update_item(item)
        self.assertEqual(item.quality, 9)
        self.assertEqual(item.sell_in, 4)

    def test_update_sell_in(self):
        """Test that update_sell_in correctly decrements the sell_in value."""
        item = Item("Normal Item", 5, 10)
        gilded_rose = GildedRose([item])
        gilded_rose.update_sell_in(item)
        self.assertEqual(item.sell_in, 4)

if __name__ == '__main__':
    unittest.main()
