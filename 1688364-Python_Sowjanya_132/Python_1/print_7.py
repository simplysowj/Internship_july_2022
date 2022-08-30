{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "9273bf8c",
   "metadata": {},
   "source": [
    "#The included code stub will read an integer,  n, from STDIN.\n",
    "\n",
    "#Without using any string methods, try to print the following:   \n",
    "      #  123...n   \n",
    "\n",
    "#Note that \"\" represents the consecutive values in between.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "771c708d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "160\n",
      "enter the valid number between 1 and 150\n"
     ]
    }
   ],
   "source": [
    "if __name__ == '__main__':\n",
    "    n = int(input())\n",
    "    \n",
    "    if (n>=1 and n <=150):\n",
    "        for i in range(n):\n",
    "            print(i+1,end=\"\")\n",
    "    else:\n",
    "        print(\"enter the valid number between 1 and 150\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "04913723",
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
