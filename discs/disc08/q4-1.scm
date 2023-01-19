;; 1 Write a function that returns the factorial of a number.
(define (factorial x) 
  (cond
    ((= x 1) 1)
    (else (* x (factorial (- x 1))))
  )
)
