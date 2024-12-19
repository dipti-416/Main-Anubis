import React, {useState} from 'react';
import AuthContext from '../../context/AuthContext';
import axios from 'axios';
import standardStatusHandler from '../../utils/standardStatusHandler';
import {useSnackbar} from 'notistack';
import Cookies from 'universal-cookie';


const checkCourseContextReset = (user) => {
  if (!user) {
    return;
  }

  const cookie = new Cookies();
  const course_context = cookie.get('course');
  if (course_context) {
    const course = JSON.parse(atob(course_context));
    const course_id = course?.id;

    if (user.admin_for.find(({id}) => id === course_id) === undefined) {
      cookie.remove('course', {path: '/'});
      window.location.reload(true);
    }
  }
};


export default function AuthWrapper({children}) {
  const {enqueueSnackbar} = useSnackbar();
  const [user, setUser] = useState(undefined);
  const [reset, setReset] = useState(0);

  React.useEffect(() => {
    axios.get('/api/public/auth/whoami').then((response) => {
      const data = standardStatusHandler(response, enqueueSnackbar);
      if (data?.user) {
        checkCourseContextReset(data.user);
        setUser({
          setReset,
          ...data.user,
        });
      } else {
        setUser(null);
      }
    });
  }, [reset]);

  return (
    <AuthContext.Provider value={user}>
      {children}
    </AuthContext.Provider>
  );
}
