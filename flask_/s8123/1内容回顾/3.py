from flask import Flask, render_template, request, redirect,session
session.clear('user_info')