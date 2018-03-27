'''import tensorflow as tf
x= tf.Variable(3, name = "x")
y= tf.Variable(4, name ="y")
f = x*x*y + y +2

with tf.Session() as sess:
	init = tf.global_variables_initializer()
	init.run() 
	print(sess.run(f))

print(f)
#updation1

def parrot_trouble(talking, hour):
    return (talking and (hour < 7 or hour > 20))
  
parrot = parrot_trouble(TRUE, 1)
print(parrot)'''
'''for i in range(1, 4):
	print(i)'''
import os
myFiles = ['accounts.txt', 'details.csv', 'invite.docx']
for i in myFiles:
        print(os.path.join('C://users//navya', i))
print(os.getcwd())

"Hello, World!"
