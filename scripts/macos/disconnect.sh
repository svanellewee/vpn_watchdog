#!/bin/bash
VPNName=$1
scutil --nc stop "$VPNName" 
