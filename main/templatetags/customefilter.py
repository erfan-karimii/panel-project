from django import template

register = template.Library()

def test(value):
    return range(value)

def number(value):
    return value / 100



register.filter('test', test)
register.filter('number', number)
