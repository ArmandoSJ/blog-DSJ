from django.http import HttpResponse
from django.template import Template, Context
from django.template.loader import get_template
from django.shortcuts import render
def home(request):
    return HttpResponse("Hola, este es el home de la aplicacion")


def suma(request, number1, number2) :

    sumTwoNumbers = number1 + number2

    printLine = """<html>
      <body>
       <h2> La suma es %s 
       </h2>
      </body>
      </html>""" % sumTwoNumbers 

    return HttpResponse(printLine)

def plantillaHtml(request):
    vName  = "Armando Salazar Jauregui"
    #vDocExterno = open("C:/Docker/django/pythonDjango/src/plantillas/parallax-template/index.html") 
    #vDocExterno = get_template('index.html')
    #vTemplate = Template(vDocExterno.read())
    #vDocExterno.close()
    vContext = Context()  

    #Context = Context({"user":vName})  
    #viewTemplate = vTemplate.render(vContext)
#C:\Docker\django\pythonDjango\src\plantillas\parallax-template\index.html
    return render(request, "index.html", vContext)
    #return HttpResponse(viewTemplate)

""" 
write a function that takes in a non-emptu array of distinct integers and an integer representing a target sum. 
If any two numbers in the input array sum up to to the target sum. the function should return them in an array,
in any order. if no two numbers sum up to the target sum, the function should return an emptu array
note that the tatget sum has to be obtained by summing two different integers in the array;
you can't add a single integer to itself in order to obtain the target sum.
you can assume that there will be at most one pait of number summing up to the tatget sum.

simple input :
array = [3,5,-4,8,11,1,-1,6]
targetSum = 10
simple output :
[-1 , 11]

"""
def twoNumberSum(array, targetSum):
    array.sort()
    left = 0
    right = len(array) - 1

    while left < right:
        currentSum = array[left]+ array[right]
        if currentSum == targetSum
          return [array[left], array[right]]
        elif currentSum < targetSum:
            left += 1
         elif currentSum > targetSum:
             right -= 1
    return []
    
def twoNumberSum(array, targetSum):
    nums = {}

    for num in array:
        potentialMatch = targetSum - num
        if potentialMatch in nums:
            return [potentialMatch, num]
            else:
                nums[num] = True
    return []


