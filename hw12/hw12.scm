(define (find s predicate)
  (cond
    ((null? s) #f)
    ((predicate (car s)) (car s))
    (else (find (cdr-stream s) predicate))
  )
)

(define (scale-stream s k)
  (if (null? s) nil
    (cons-stream (* (car s) k) (scale-stream (cdr-stream s) k))
  )
)

(define (has-cycle m-stream)
  (define (m-cycler s)
    (cond
      ((null? (cdr-stream s)) #f)
      ((eq? s m-stream) #t)
      (else (m-cycler (cdr-stream s)))
    )
  )
  (if (null? m-stream) #f
    (m-cycler (cdr-stream m-stream))
  )
)

(define (has-cycle-constant s)
  'YOUR-CODE-HERE
)
