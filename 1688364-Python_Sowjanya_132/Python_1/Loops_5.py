{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "07657ac8",
   "metadata": {},
   "outputs": [],
   "source": [
    "#Task\n",
    "#The provided code stub reads and integer,n , from STDIN. For all non-negative integers i<n , print i*i."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "52b675df",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "ENter the value between 1 and 20  :  5\n",
      "0\n",
      "1\n",
      "4\n",
      "9\n",
      "16\n"
     ]
    }
   ],
   "source": [
    "n = int(input(\"ENter the value between 1 and 20  :  \"))\n",
    "\n",
    "for i in range(n):\n",
    "        if(n>=1 and n<=20):\n",
    "            print (i * i)\n",
    "        else:\n",
    "            print(\"Enter the value between 1 and 20\")\n",
    "            break"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "96ef659f",
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
