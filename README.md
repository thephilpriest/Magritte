# Magritte


![Ceci n'est pas une pipe](MagrittePipe.jpg?raw=t)

This project simulates arbitrary objects flowing through a pipe. 

It's written in Python

It's a passion project

The objects in this pipe are formally referred to as `smidgeons`. There may be better names for this, but I think that word is cute so that's what I'm using. Also, the word "object", although not strictly a reserve word in Python, would be really misleading since this implementation is object oriented.

The smidgeons in the pipe are considered to each be autonomous in that they are all capable of accelerating by means of applying force that they themselves create - IE, not due to force being applied to them externally. Specifically, this allows me to simulate traffic flows where each smidgeon is akin to a car and the pipe is akin to a lane of traffic.

A smidgeon may also be subjected to acceleration by the smidgeon behind it colliding with it and pushing it forward. This scenario allows me to simulate things that at least on their face are closer to models of fluid dynamics.

In version 1.0 the pipe is only 1 smidgeon wide.

The user can declare whether each smidgeon is identical or not and if not, parameters dictating the ranges of values they can be generated with and the statistics about them; specifically the mean and standard deviation for all the values.

The user can also declare whether the smidgeons will have autonomous movement or be under pressure at entry; the latter implying that the smidgeons will not have any gaps between them.

The user can declare flow interruptions. This is in fact the entire reason for this project. To see what happens to the smidgeons if one of them "does something silly" to disrupt the flow of traffic. The interruptions can be slow-downs or stops and need to be described in terms that assert: the rate of the slowdown, the duration of the slowdown, the rate of the speed-back-up and the speed both before and after the event