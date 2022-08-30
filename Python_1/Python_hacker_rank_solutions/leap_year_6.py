{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "7e8dea64",
   "metadata": {},
   "source": [
    "Task\n",
    "\n",
    "Given a year, determine whether it is a leap year. If it is a leap year, return the Boolean True, otherwise return False.\n",
    "\n",
    "Note that the code stub provided reads from STDIN and passes arguments to the is_leap function. It is only necessary to complete the is_leap function.\n",
    "\n",
    "Constraints\n",
    " year>=1900 and year<=100000\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "d9c9f3d3",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "100000\n",
      "True\n"
     ]
    }
   ],
   "source": [
    "def is_leap(year):\n",
    "    \n",
    "    if(year>=1900 and year<=100000):\n",
    "        leap = False\n",
    "        if(year %400 == 0):\n",
    "            leap = True\n",
    "        elif year % 100 ==0:\n",
    "            leap =False\n",
    "        elif year % 4 == 0:\n",
    "            leap = True\n",
    "        print(leap)\n",
    "    else :\n",
    "        print(\"ENter valid number between 1900 and 100,000\")\n",
    "       \n",
    "  \n",
    "    \n",
    "    \n",
    "\n",
    "year = int(input())\n",
    "is_leap(year)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f5c71fe2",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
